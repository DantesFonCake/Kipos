package com.example.kipos.network;

import com.example.kipos.data.json.telemetry.Telemetry;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface KiposApi {
    @GET("/module/telemetry/{uuid}")
    public Call<List<Telemetry>> getTelemetryWithUuid(@Path("uuid") int uuid);
}
