package com.example.kiposend.ui.recycler;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.kiposend.R;

import org.jetbrains.annotations.NotNull;

import java.util.List;

public class ModuleAdapter extends RecyclerView.Adapter<ModuleAdapter.ViewHolder>{
    private final LayoutInflater inflater;
    private List<Module> moduleList;


    public ModuleAdapter(Context context, List<Module> moduleList) {
        this.inflater = LayoutInflater.from(context);
        this.moduleList = moduleList;
    }


    @NonNull
    @NotNull
    @Override
    public ModuleAdapter.ViewHolder onCreateViewHolder(@NonNull @NotNull ViewGroup parent, int viewType) {

        View view = inflater.inflate(R.layout.module_item, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(ModuleAdapter.ViewHolder holder, int position) {

        Module module = moduleList.get(position);
        //передаем к карточку имя модуля
        holder.nameView.setText(module.getName());
        //передаем статус
        if (module.lvlHumidity <= module.targetHumidity/2){
            holder.statusView.setText("low humidity");
        } else if (module.lvlConcentrate <= 20){
            holder.statusView.setText("low concentrate");
        } else if (module.temperature <= module.targetTemperature/2){
            holder.statusView.setText("low temperature");
        } else if (module.lvlWater <= 20){
            holder.statusView.setText("low level water");
        } else {
            holder.statusView.setText("OK");
        }

    }

    @Override
    public int getItemCount() {
        return moduleList.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {

        final TextView nameView;
        final TextView statusView;

        public ViewHolder(@NonNull @NotNull View itemView) {
            super(itemView);
            nameView = (TextView) itemView.findViewById(R.id.nameModule);
            statusView = (TextView) itemView.findViewById(R.id.statusModule);
        }
    }
}
