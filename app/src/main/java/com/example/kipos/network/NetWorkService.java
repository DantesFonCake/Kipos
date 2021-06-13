package com.example.kipos.network;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class NetWorkService {

    private static NetWorkService mInstance;
    private static final String BASE_URL = "http://<address>/kipos";
    private Retrofit retrofit;

    private NetWorkService(){
        retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
    }

    public static NetWorkService getInstance() {
        if(mInstance == null){
            mInstance = new NetWorkService();
        }
        return mInstance;
    }

    public KiposApi getKiposApi(){
        return retrofit.create(KiposApi.class);
    }
}
