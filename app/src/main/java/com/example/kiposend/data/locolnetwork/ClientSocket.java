package com.example.kiposend.data.locolnetwork;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.Socket;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.Arrays;

public class ClientSocket {
    private String severIp = null;
    private OnMessageReceived messageListener = null;
    private boolean mRun = false;
    private DatagramSocket UdpSocket;
    private PrintWriter bufferOut;
    private BufferedReader bufferIn;
    private Socket TcpSocket;
    private String serverMessage;

    public ClientSocket(OnMessageReceived messageListener) throws IOException {
        this.messageListener = messageListener;
    }

    public DatagramSocket getUdpSocket() throws IOException {
        if (UdpSocket == null){
            UdpSocket = new DatagramSocket(37020, InetAddress.getByName("0.0.0.0"));
            UdpSocket.setBroadcast(true);
        }
        return UdpSocket;
    }

    public void sendMessage(String message){
        if (bufferOut != null && !bufferOut.checkError()){
            bufferOut.println(message);
            bufferOut.flush();
        }
    }

    public void connectToServer(){
        try {
            UdpSocket = new DatagramSocket(37020, InetAddress.getByName("0.0.0.0"));
            UdpSocket.setBroadcast(true);

            DatagramPacket packet = new DatagramPacket(new byte[16], 16);

            UdpSocket.receive(packet);
            severIp = Arrays.toString(packet.getData());
            messageListener.onConnected();

        } catch (SocketException e) {
            e.printStackTrace();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (UdpSocket != null && UdpSocket.isConnected()){
                UdpSocket.close();
            }
        }
    }

    public void received(String address) {
        try {
            TcpSocket = new Socket(InetAddress.getByName(address), 12345);
            mRun = true;
            bufferOut = new PrintWriter(new BufferedWriter(new OutputStreamWriter(TcpSocket.getOutputStream())), true);
            bufferIn = new BufferedReader(new InputStreamReader(TcpSocket.getInputStream()));

            while (mRun){
                if (bufferOut.checkError()){
                    mRun = false;
                }

                serverMessage = bufferIn.readLine();

                if (serverMessage != null && messageListener != null){
                    messageListener.messageReceived(serverMessage);
                }
            }
        } catch (IOException e){
        } catch (UnknownError error){
        } finally {
            if (TcpSocket != null && TcpSocket.isConnected()){
                try {
                    TcpSocket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }

    public String getSeverIp() {
        return severIp;
    }

    public String getServerMessage() {
        return serverMessage;
    }

    public void stopClient(){
        mRun = false;

        if (bufferOut != null){
            bufferOut.flush();
            bufferOut.close();
        }

        messageListener = null;
        bufferOut = null;
        bufferIn = null;
        serverMessage = null;
    }

    public boolean isConnect(){
        return TcpSocket !=null && TcpSocket.isConnected();
    }

    public boolean isRunning() {
        return mRun;
    }

    public interface OnMessageReceived{
        void messageReceived(String message);
        void onConnected();
    }
}
