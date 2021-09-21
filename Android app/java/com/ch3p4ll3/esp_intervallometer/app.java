package com.ch3p4ll3.esp_intervallometer;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import com.ch3p4ll3.esp_intervallometer.ui.main.SectionsPagerAdapter;
import com.google.android.material.tabs.TabLayout;

import java.io.IOException;

public class app extends AppCompatActivity {
    private Button stop_btn;
    private String macAdd;
    private static TextView status;
    private CheckBox autofocus;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        macAdd = getIntent().getStringExtra("macAddr");

        setContentView(R.layout.app);
        SectionsPagerAdapter sectionsPagerAdapter = new SectionsPagerAdapter(this, getSupportFragmentManager(), macAdd);
        ViewPager viewPager = findViewById(R.id.view_pager);
        viewPager.setAdapter(sectionsPagerAdapter);
        TabLayout tabs = findViewById(R.id.tabs);
        tabs.setupWithViewPager(viewPager);

        stop_btn = (Button) findViewById(R.id.stop_btn);
        status = (TextView) findViewById(R.id.status);
        autofocus = (CheckBox) findViewById(R.id.afCheck);
        stop_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(view.getContext(), "Stop", Toast.LENGTH_SHORT).show();
                MainActivity.sendStop();
            }
        });

        autofocus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(view.getContext(), "Autofocus", Toast.LENGTH_SHORT).show();
                MainActivity.sendAf(autofocus.isChecked() ? 1 : 0);
            }
        });
    }

    @Override
    protected void onDestroy() {
        MainActivity.destroy();
        super.onDestroy();
    }
}
