package com.example.kiposend.activities;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

import com.example.kiposend.R;

public class ModuleActivity extends AppCompatActivity {

    TextView nameView;
    TextView lvlHimView;
    EditText targetHim;
    TextView temperatureView;
    EditText targetTemp;
    TextView lvlWaterView;
    TextView lvlConView;
    EditText wifiName;
    EditText wifiPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_module_acrivity);

        initUi();
        intentToContent();

    }

    private void initUi(){
        nameView = (TextView) findViewById(R.id.nameMod);
        lvlHimView = (TextView) findViewById(R.id.lvlHim);
        targetHim = (EditText) findViewById(R.id.targetHim);
        temperatureView = (TextView) findViewById(R.id.temperature);
        targetTemp = (EditText) findViewById(R.id.targetTemparature);
        lvlWaterView = (TextView) findViewById(R.id.lvlWater);
        lvlConView = (TextView) findViewById(R.id.lvlConcentrate);
        wifiName = (EditText) findViewById(R.id.nameWifi);
        wifiPassword = (EditText) findViewById(R.id.wifiPas);
    }

    private void intentToContent(){
        nameView.setText(getIntent().getExtras().getString("name"));
        lvlHimView.setText(getIntent().getExtras().getString("lvlHim"));
        targetHim.setText(getIntent().getExtras().getString("targetHim"));
        temperatureView.setText(getIntent().getExtras().getString("temp"));
        targetTemp.setText(getIntent().getExtras().getString("targetTemp"));
        lvlWaterView.setText(getIntent().getExtras().getString("lvlWater"));
        lvlConView.setText(getIntent().getExtras().getString("lvlCon"));
        wifiName.setText(getIntent().getExtras().getString("wifiName"));
        wifiPassword.setText(getIntent().getExtras().getString("wifiPas"));
    }
}