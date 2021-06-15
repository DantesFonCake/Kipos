package com.example.kiposend.data.json.settings;

import com.google.gson.annotations.SerializedName;

public class ClimateSet {
    @SerializedName("target_temperature")
    public int temperature;
    @SerializedName("target_humidity")
    public int humidity;
    @SerializedName("start_time")
    public int startTime;
    @SerializedName("end_time")
    public int endTime;

    public ClimateSet(int temperature, int humidity, int startTime, int endTime) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    public int getTemperature() {
        return temperature;
    }

    public void setTemperature(int temperature) {
        this.temperature = temperature;
    }

    public int getHumidity() {
        return humidity;
    }

    public void setHumidity(int humidity) {
        this.humidity = humidity;
    }

    public int getStartTime() {
        return startTime;
    }

    public void setStartTime(int startTime) {
        this.startTime = startTime;
    }

    public int getEndTime() {
        return endTime;
    }

    public void setEndTime(int endTime) {
        this.endTime = endTime;
    }

    @Override
    public String toString() {
        return "ClimateSet{" +
                "temperature=" + temperature +
                ", humidity=" + humidity +
                ", startTime=" + startTime +
                ", endTime=" + endTime +
                '}';
    }
}
