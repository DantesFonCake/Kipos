package com.example.kipos.localnetwork;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Arrays;

public class ClientSocket {

    private String severMessage;
    private OnMessageReceived messageListener = null;
    private boolean mRun = false;
    private DatagramSocket socket;
    private String address;

    public ClientSocket(OnMessageReceived messageListener, String address) {
        this.messageListener = messageListener;
        this.address = address;
    }

    public DatagramSocket getReceivedSocket() throws IOException {
        if (socket == null){
            socket = new DatagramSocket(8002, InetAddress.getByName("0.0.0.0"));
            socket.setBroadcast(true);
        }
        return socket;
    }

    public void run() {
        try {
            mRun = true;
            messageListener.onConnected();

            while (mRun){
               DatagramPacket packet = new DatagramPacket(new byte[1], 1);
               socket.receive(packet);
               severMessage = Arrays.toString(packet.getData());

               if (severMessage != null && messageListener != null){
                   messageListener.messageReceived(severMessage);
               }
            }
        } catch (IOException e){
        } finally {
            if (socket != null && socket.isConnected()){
                socket.close();
            }
        }
    }

    public void stopClient(){
        mRun = false;
        messageListener = null;
        severMessage = null;
    }

    public boolean isConnect(){
        return socket !=null && socket.isConnected();
    }

    public boolean isRunning() {
        return mRun;
    }

    public interface OnMessageReceived{
        void messageReceived(String message);
        void onConnected();
    }
}
