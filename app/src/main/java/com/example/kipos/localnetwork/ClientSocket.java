package com.example.kipos.localnetwork;

import android.widget.Toast;

import org.jetbrains.annotations.NotNull;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Arrays;


public class ClientSocket {

    private String severMessage;
    private OnMessageReceived messageListener = null;
    private boolean mRun = false;
    private DatagramSocket socket;

    public ClientSocket(OnMessageReceived messageListener) {
        this.messageListener = messageListener;
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
            socket = new DatagramSocket(37020, InetAddress.getByName("0.0.0.0"));
            mRun = true;
            messageListener.onConnected();

            while (mRun){
                DatagramPacket packet = new DatagramPacket(new byte[1], 16);
                socket.receive(packet);
                severMessage = Arrays.toString(packet.getData());

                if (severMessage != null && messageListener != null){
                    messageListener.messageReceived(severMessage);
                }
            }
        } catch (IOException e){
        } catch (UnknownError error){
        } finally {
            if (socket != null && socket.isConnected()){
                socket.close();
            }
        }

    }

    public String getSeverMessage() {
        return severMessage;
    }

    public void stopClient(){
        mRun = false;
        messageListener = null;
        severMessage = null;
        if (socket != null){
            socket.close();
        }
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
