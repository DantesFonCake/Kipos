package com.example.kiposend.data.json.telemetry;

public class Telemetry {
    public static Message message;
    public int uuid;

    public Telemetry(Message message, int uuid) {
        this.message = message;
        this.uuid = uuid;
    }

    public Message getMessage() {
        return message;
    }

    public void setMessage(Message message) {
        this.message = message;
    }

    public int getUuid() {
        return uuid;
    }

    public void setUuid(int uuid) {
        this.uuid = uuid;
    }

    @Override
    public String toString() {
        return "Telemetry{" +
                "message=" + message +
                ", uuid=" + uuid +
                '}';
    }
}
