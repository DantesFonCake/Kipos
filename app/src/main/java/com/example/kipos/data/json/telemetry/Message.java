package com.example.kipos.data.json.telemetry;

import androidx.annotation.Nullable;

import com.google.gson.annotations.SerializedName;

public class Message {

    public float humidity;
    public float temperature;
    @SerializedName("water_level") @Nullable
    public float waterLvl;
    @SerializedName("concentrate_level") @Nullable
    public float concentrLvl;

    public Message(float humidity, float temperature, float waterLvl, float concentrLvl) {
        this.humidity = humidity;
        this.temperature = temperature;
        this.waterLvl = waterLvl;
        this.concentrLvl = concentrLvl;
    }

    public float getHumidity() {
        return humidity;
    }

    public void setHumidity(float humidity) {
        this.humidity = humidity;
    }

    public float getTemperature() {
        return temperature;
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
    }

    public float getWaterLvl() {
        return waterLvl;
    }

    public void setWaterLvl(float waterLvl) {
        this.waterLvl = waterLvl;
    }

    public float getConcentrLvl() {
        return concentrLvl;
    }

    public void setConcentrLvl(float concentrLvl) {
        this.concentrLvl = concentrLvl;
    }

    @Override
    public String toString() {
        return "Message{" +
                "humidity=" + humidity +
                ", temperature=" + temperature +
                ", waterLvl=" + waterLvl +
                ", concentrLvl=" + concentrLvl +
                '}';
    }
}
