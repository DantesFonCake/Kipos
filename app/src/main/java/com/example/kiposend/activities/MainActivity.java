package com.example.kiposend.activities;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.Toast;

import com.example.kiposend.R;
import com.example.kiposend.data.locolnetwork.ClientSocket;
import com.example.kiposend.ui.recycler.Module;
import com.example.kiposend.ui.recycler.ModuleAdapter;

import java.io.IOException;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    ArrayList<Module> modules = new ArrayList<Module>();
    private ClientSocket client;
    private String serverMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        connect();

        RecyclerView recyclerView = findViewById(R.id.moduleRecycler);
        ModuleAdapter adapter = new ModuleAdapter(this, modules);
        recyclerView.setAdapter(adapter);
    }

    private void connect(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    client = new ClientSocket(new ClientSocket.OnMessageReceived() {
                        @Override
                        public void onConnected() {
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    if (client.getSeverIp() != null){
                                        Toast.makeText(MainActivity.this, "ip received", Toast.LENGTH_LONG).show();
                                    }
                                }
                            });
                        }

                        @Override
                        public void messageReceived(String message) {
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    client.received(client.getSeverIp());
                                    if (client.getServerMessage() != null){
                                        serverMessage = client.getServerMessage();
                                    }
                                }
                            });
                        }
                    });
                } catch (IOException e) {
                    e.printStackTrace();
                }
                client.connectToServer();
            }
        }).start();
    }

    private void setInitData(){

    }
}