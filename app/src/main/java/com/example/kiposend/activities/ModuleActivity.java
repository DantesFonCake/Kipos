package com.example.kiposend.activities;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

import com.example.kiposend.R;
import com.example.kiposend.ui.recycler.Module;

public class ModuleActivity extends AppCompatActivity {

    TextView nameView;
    TextView lvlHimView;
    EditText targetHimView;
    TextView temperatureView;
    EditText targetTempView;
    TextView lvlWaterView;
    TextView lvlConView;
    EditText wifiNameView;
    EditText wifiPasswordView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_module_acrivity);

        initUi();
        intentToContent();

    }

    private void initUi(){
        nameView = findViewById(R.id.nameMod);
        lvlHimView = findViewById(R.id.lvlHim);
        targetHimView = findViewById(R.id.targetHim);
        temperatureView = findViewById(R.id.temperature);
        targetTempView = findViewById(R.id.targetTemparature);
        lvlWaterView = findViewById(R.id.lvlWater);
        lvlConView = findViewById(R.id.lvlConcentrate);
        wifiNameView = findViewById(R.id.nameWifi);
        wifiPasswordView = findViewById(R.id.wifiPas);
    }

    private void intentToContent(){
        Intent intent = getIntent();

        Module module = intent.getParcelableExtra("name");
        nameView.setText(module.name);
        lvlHimView.setText(module.lvlHumidity);
        targetHimView.setText(module.targetHumidity);
        temperatureView.setText(module.temperature);
        targetTempView.setText(module.targetTemperature);
        lvlWaterView.setText(module.lvlWater);
        lvlConView.setText(module.lvlConcentrate);
        wifiNameView.setText(intent.getExtras().getString("wifiName"));
        wifiPasswordView.setText(intent.getExtras().getString("wifiPas"));
    }
}