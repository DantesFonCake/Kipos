package com.example.kiposend.data.json;

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
