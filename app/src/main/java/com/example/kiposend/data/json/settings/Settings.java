package com.example.kiposend.data.json.settings;

import com.google.gson.annotations.SerializedName;

public class Settings {
    public ControllerSet controllerSet;
    public ClimateSet climateSet;
    @SerializedName("last_update_time")
    public int lastUpTime;

    public Settings(ControllerSet controllerSet, ClimateSet climateSet, int lastUpTime) {
        this.controllerSet = controllerSet;
        this.climateSet = climateSet;
        this.lastUpTime = lastUpTime;
    }

    public ControllerSet getControllerSet() {
        return controllerSet;
    }

    public void setControllerSet(ControllerSet controllerSet) {
        this.controllerSet = controllerSet;
    }

    public int getLastUpTime() {
        return lastUpTime;
    }

    public void setLastUpTime(int lastUpTime) {
        this.lastUpTime = lastUpTime;
    }

    public ClimateSet getClimateSet() {
        return climateSet;
    }

    public void setClimateSet(ClimateSet climateSet) {
        this.climateSet = climateSet;
    }

    @Override
    public String toString() {
        return "Settings{" +
                "controllerSet=" + controllerSet +
                ", climateSet=" + climateSet +
                '}';
    }
}
