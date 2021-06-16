package com.example.kiposend.ui.recycler;

import androidx.annotation.Nullable;


public class Module {
    public String name;
    public float lvlHumidity;
    public int targetHumidity;
    public float temperature;
    public int targetTemperature;
    @Nullable
    public float lvlWater;
    @Nullable
    public float lvlConcentrate;
    public String wifiName;
    public String wifiPass;

    public Module(String name, float lvlHumidity, int targetHumidity, float temperature, int targetTemperature, float lvlWater, float lvlConcentrate, String wifiName, String wifiPass) {
        this.name = name;
        this.lvlHumidity = lvlHumidity;
        this.targetHumidity = targetHumidity;
        this.temperature = temperature;
        this.targetTemperature = targetTemperature;
        this.lvlWater = lvlWater;
        this.lvlConcentrate = lvlConcentrate;
        this.wifiName = wifiName;
        this.wifiPass = wifiPass;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public float getLvlHumidity() {
        return lvlHumidity;
    }

    public void setLvlHumidity(float lvlHumidity) {
        this.lvlHumidity = lvlHumidity;
    }

    public int getTargetHumidity() {
        return targetHumidity;
    }

    public void setTargetHumidity(int targetHumidity) {
        this.targetHumidity = targetHumidity;
    }

    public float getTemperature() {
        return temperature;
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
    }

    public int getTargetTemperature() {
        return targetTemperature;
    }

    public void setTargetTemperature(int targetTemperature) {
        this.targetTemperature = targetTemperature;
    }

    public float getLvlWater() {
        return lvlWater;
    }

    public void setLvlWater(float lvlWater) {
        this.lvlWater = lvlWater;
    }

    public float getLvlConcentrate() {
        return lvlConcentrate;
    }

    public void setLvlConcentrate(float lvlConcentrate) {
        this.lvlConcentrate = lvlConcentrate;
    }

    public String getWifiName() {
        return wifiName;
    }

    public void setWifiName(String wifiName) {
        this.wifiName = wifiName;
    }

    public String getWifiPass() {
        return wifiPass;
    }

    public void setWifiPass(String wifiPass) {
        this.wifiPass = wifiPass;
    }

    @Override
    public String toString() {
        return "Module{" +
                "name='" + name + '\'' +
                ", lvlHumidity=" + lvlHumidity +
                ", targetHumidity=" + targetHumidity +
                ", temperature=" + temperature +
                ", targetTemperature=" + targetTemperature +
                ", lvlWater=" + lvlWater +
                ", lvlConcentrate=" + lvlConcentrate +
                ", wifiName='" + wifiName + '\'' +
                ", wifiPass='" + wifiPass + '\'' +
                '}';
    }
}
