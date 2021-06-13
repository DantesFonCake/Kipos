package com.example.kipos.data.json.settings;

import com.google.gson.annotations.SerializedName;

public class ControllerSet {

    @SerializedName("initialized")
    public String init;
    public String ssid;
    public String pas;
    public String name;
    @SerializedName("time_zone")
    public int timeZone;

    public ControllerSet(String init, String ssid, String pas, String name, int timeZone) {
        this.init = init;
        this.ssid = ssid;
        this.pas = pas;
        this.name = name;
        this.timeZone = timeZone;
    }

    public String getInit() {
        return init;
    }

    public void setInit(String init) {
        this.init = init;
    }

    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }

    public String getPas() {
        return pas;
    }

    public void setPas(String pas) {
        this.pas = pas;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getTimeZone() {
        return timeZone;
    }

    public void setTimeZone(int timeZone) {
        this.timeZone = timeZone;
    }

    @Override
    public String toString() {
        return "ControllerSet{" +
                "init='" + init + '\'' +
                ", ssid='" + ssid + '\'' +
                ", pas='" + pas + '\'' +
                ", name='" + name + '\'' +
                ", timeZone=" + timeZone +
                '}';
    }
}
