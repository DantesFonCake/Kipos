package com.example.kiposend.activities;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.os.Parcelable;
import android.widget.Toast;

import com.example.kiposend.R;
import com.example.kiposend.data.locolnetwork.ClientSocket;
import com.example.kiposend.data.locolnetwork.UdpSweeper;
import com.example.kiposend.ui.recycler.Module;
import com.example.kiposend.ui.recycler.ModuleAdapter;

import java.util.ArrayList;
import java.util.List;
import java.util.Timer;

public class MainActivity extends AppCompatActivity {

    ArrayList<Module> modules = new ArrayList<Module>();
    private ClientSocket client;
    private UdpSweeper udpSweeper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


//        Toast.makeText(MainActivity.this, "start connect", Toast.LENGTH_SHORT).show();
//        connect();

        setInitData();
        RecyclerView recyclerView = (RecyclerView) findViewById(R.id.moduleRecycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));


        ModuleAdapter.OnModuleClickListener moduleClickListener = new ModuleAdapter.OnModuleClickListener() {
            @Override
            public void onModuleClick(Module module, int position) {
                Intent intent = new Intent(MainActivity.this, ModuleActivity.class);
                intent.putExtra("name", module);

                startActivity(intent);
            }
        };

        ModuleAdapter adapter = new ModuleAdapter(this, modules, moduleClickListener);
        recyclerView.setAdapter(adapter);
    }

    private void connect(){

        udpSweeper = new UdpSweeper(37020, 16, 30);
        udpSweeper.start();

//        new Thread(new Runnable() {
//            @Override
//            public void run() {
//
//            }
//        }).start();
    }

    private void setInitData(){
        modules.add(new Module("Angel",  85, 90,  30, 29, 50, 50, "Example", "12345678"));
        modules.add(new Module("Doom",  60, 49,  45, 16, 90, 79, "WiFi", "19242642"));
    }
}