package com.example.kiposend.data.json;

import android.content.Context;

import com.example.kiposend.data.json.telemetry.Telemetry;
import com.google.gson.Gson;

import java.io.FileOutputStream;
import java.io.IOException;

public class JsonHelper {

        static boolean exportToJsonTelemetry(Context context, Telemetry telemetry){

        Gson gson = new Gson();
        String jsonStr = gson.toJson(telemetry);

        FileOutputStream fileOutputStream = null;

        try{
//            fileOutputStream = context.openFileOutput(!!взять строку из приходящей телеметрии!!, context.MODE_PRIVATE);
//            fileOutputStream.write(jsonStr.getBytes());
            return true;
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            if (fileOutputStream != null){
                try {
                    fileOutputStream.close();
                } catch (IOException e){
                    e.printStackTrace();
                }
            }
        }

        return false;
    }
}
