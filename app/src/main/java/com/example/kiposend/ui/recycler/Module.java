package com.example.kiposend.ui.recycler;

import android.os.Parcel;
import android.os.Parcelable;

import androidx.annotation.Nullable;


public class Module implements Parcelable {
    public String name;
    public int lvlHumidity;
    public int targetHumidity;
    public int temperature;
    public int targetTemperature;
    @Nullable
    public int lvlWater;
    @Nullable
    public int lvlConcentrate;
    public String wifiName;
    public String wifiPass;

    public Module(String name, int lvlHumidity, int targetHumidity, int temperature, int targetTemperature, int lvlWater, int lvlConcentrate, String wifiName, String wifiPass) {
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

    public Module(Parcel source) {
        name = source.readString();
        lvlHumidity = source.readInt();
        targetHumidity = source.readInt();
        temperature = source.readInt();
        targetTemperature = source.readInt();
        lvlWater = source.readInt();
        lvlConcentrate = source.readInt();
        wifiName = source.readString();
        wifiPass = source.readString();
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

    public void setLvlHumidity(int lvlHumidity) {
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

    public void setTemperature(int temperature) {
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

    public void setLvlWater(int lvlWater) {
        this.lvlWater = lvlWater;
    }

    public float getLvlConcentrate() {
        return lvlConcentrate;
    }

    public void setLvlConcentrate(int lvlConcentrate) {
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

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(name);
        dest.writeFloat(lvlHumidity);
        dest.writeInt(targetHumidity);
        dest.writeFloat(temperature);
        dest.writeInt(targetTemperature);
        dest.writeFloat(lvlWater);
        dest.writeFloat(lvlConcentrate);
        dest.writeString(wifiName);
        dest.writeString(wifiPass);
    }

    public static final Parcelable.Creator<Module> CREATOR = new Parcelable.Creator<Module>(){

        @Override
        public Module createFromParcel(Parcel source) {
            return new Module(source);
        }

        @Override
        public Module[] newArray(int size) {
            return new Module[size];
        }
    };
}
