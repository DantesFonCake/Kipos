package com.example.kipos.data.json;

import android.content.Context;
import android.provider.ContactsContract;

import com.example.kipos.data.json.telemetry.Telemetry;
import com.google.gson.Gson;

import java.io.FileOutputStream;
import java.io.IOException;

public class JsonHelper {

//    static boolean exportToJsonTelemetry(Context context, Telemetry telemetry){
//
//        Gson gson = new Gson();
//        String jsonStr = gson.toJson(telemetry);
//
//        FileOutputStream fileOutputStream = null;
//
//        try{
//            fileOutputStream = context.openFileOutput(, context.MODE_PRIVATE);
//            fileOutputStream.write(jsonStr.getBytes());
//            return true;
//        } catch (Exception e){
//            e.printStackTrace();
//        } finally {
//            if (fileOutputStream != null){
//                try {
//                    fileOutputStream.close();
//                } catch (IOException e){
//                    e.printStackTrace();
//                }
//            }
//        }
//
//        return false;
//    }


}
