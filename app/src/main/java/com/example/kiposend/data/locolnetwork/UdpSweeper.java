package com.example.kiposend.data.locolnetwork;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;
import java.net.SocketTimeoutException;
import java.nio.charset.StandardCharsets;
import java.util.Iterator;
import java.util.concurrent.ConcurrentLinkedQueue;

public class UdpSweeper extends Thread{
    int port;
    int bufferSize;
    int messageTimeout;
    public Boolean Running = false;

    public UdpSweeper(int port, int bufferSize, int messageTimeout) {
        this.port = port;
        this.bufferSize = bufferSize;
        this.messageTimeout = messageTimeout;
    }

    ConcurrentLinkedQueue<UdpMessage<String>> _messages = new ConcurrentLinkedQueue<>();

    public Iterable<String> messages = () -> {
        Iterator<UdpMessage<String>> it = _messages.iterator();
        return new Iterator<String>() {
            @Override
            public boolean hasNext() {
                return it.hasNext();
            }

            @Override
            public String next() {
                return it.next().GetMessage();
            }
        };
    };


    @Override
    public void run() {
        Running = true;
        DatagramSocket sock;
        DatagramPacket packet = new DatagramPacket(new byte[bufferSize], bufferSize);
        try {
            sock = new DatagramSocket(port);
            sock.setBroadcast(true);
            sock.setSoTimeout(1000);
        } catch (SocketException e) {
            e.printStackTrace();
            throw new RuntimeException(String.format("Failed to bind socket to port: %d", port));
        }
        boolean getTimeout;
        while (Running) {
            try {
                sock.receive(packet);
                getTimeout = false;
            } catch (SocketTimeoutException e) {
                getTimeout = true;
            } catch (IOException e) {
                e.printStackTrace();
                throw new RuntimeException("Get IOException");
            }

            String message = null;
            if (!getTimeout)
                message = new String(packet.getData(), StandardCharsets.US_ASCII).trim();
            boolean contains = false;
            for (UdpMessage<String> m : _messages) {
                if (!getTimeout && message.equals(m.GetMessage())) {
                    m.Revalidate();
                    contains = true;
                } else
                    m.IncreaseAge();
            }
            if (!contains && message != null)
                _messages.add(new UdpMessage<>(message, messageTimeout));

            _messages.removeIf(stringUDPMessage -> !stringUDPMessage.IsValid());
            packet = new DatagramPacket(new byte[bufferSize], bufferSize);
        }
    }
}
