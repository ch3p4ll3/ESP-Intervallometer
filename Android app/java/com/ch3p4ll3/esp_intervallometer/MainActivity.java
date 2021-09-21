package com.ch3p4ll3.esp_intervallometer;

import android.annotation.SuppressLint;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothHeadset;
import android.bluetooth.BluetoothSocket;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;

import com.google.android.material.tabs.TabLayout;
import androidx.viewpager.widget.ViewPager;
import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.ch3p4ll3.esp_intervallometer.ui.main.SectionsPagerAdapter;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.text.BreakIterator;
import java.util.ArrayList;
import java.util.Set;
import java.util.UUID;


public class MainActivity extends AppCompatActivity {

    private static ConnectedThread connectedThread;
    private ListView listView;
    private ArrayList<String> mDeviceList = new ArrayList<String>();
    private BluetoothAdapter mBluetoothAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.main);

        listView = (ListView) findViewById(R.id.listView);
        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        if (!mBluetoothAdapter.isEnabled()) {
            startActivityForResult(new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE),1);
        }

        Set<BluetoothDevice> pairedDevices = mBluetoothAdapter.getBondedDevices();
        ArrayList<String> devices = new ArrayList<>();
        for (BluetoothDevice bt : pairedDevices) {
            devices.add(bt.getName() + "\n" + bt.getAddress());
        }
        ArrayAdapter arrayAdapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, devices);
        listView.setAdapter(arrayAdapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            public void onItemClick(AdapterView<?> adapter, View v, int position, long id) {
                String MacAddress = (String) adapter.getItemAtPosition(position);
                MacAddress = MacAddress.split("\n")[1];


                connectedThread = new ConnectedThread(MacAddress);
                connectedThread.start();

                Intent intent = new Intent(MainActivity.this, app.class);
                intent.putExtra("macAddr", MacAddress);
                startActivity(intent);
            }
        });
    }

    public static void sendStop(){
        connectedThread.write("stop#");
    }

    public static void sendAf(int isChecked){
        connectedThread.write("af#"+isChecked);
    }

    public static void sendSingleShot(){
        connectedThread.write("singleShot#");
    }

    public static void sendBulb(){
        connectedThread.write("Bulb#");
    }

    public static void sendTimerbulb(String seconds){
        connectedThread.write("timerBulb#"+seconds);
    }

    public static void sendIntervallometer(String delay, String shots){
        connectedThread.write("intervallometer#"+delay+"#"+shots);
    }

    public static void sendBulbIntervallometer(String delay, String bulbDuration, String shots){
        connectedThread.write("bulbIntervallometer#"+delay+"#"+bulbDuration+"#"+shots);
    }

    public static void destroy() {
        try{
            connectedThread.disconnect();
        } catch (Exception e){

        }
        connectedThread.interrupt();
    }
}
