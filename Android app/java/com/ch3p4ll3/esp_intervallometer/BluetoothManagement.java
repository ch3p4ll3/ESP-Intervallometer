package com.ch3p4ll3.esp_intervallometer;
/*
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Context;
import android.widget.Toast;

import java.io.IOException;
import java.io.OutputStream;
import java.util.UUID;

class BlManagement {
        private static BluetoothAdapter mBluetoothAdapter;
        private static BluetoothDevice mmDevice;
        private static BluetoothSocket mmSocket;
        private static OutputStream outStream;

        private static UUID uuid = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");

        public static void connect(Context ct, String macAddr, String message){
                mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
                if (mBluetoothAdapter == null){
                        // IL BLUETOOTH NON E' SUPPORTATO
                        Toast.makeText(ct, "BlueTooth non supportato", Toast.LENGTH_LONG).show();
                } else {
                        if (!mBluetoothAdapter.isEnabled()) {
                                Toast.makeText(ct, "BlueTooth non abilitato", Toast.LENGTH_LONG).show();
                        } else {
                                mmDevice=mBluetoothAdapter.getRemoteDevice(macAddr);
                                try{
                                        mmSocket=mmDevice.createRfcommSocketToServiceRecord(uuid);
                                }
                                catch (IOException e){
                                }
                                try{
                                        mmSocket.connect();
                                        outStream = mmSocket.getOutputStream();
                                        sendMessageBluetooth(message, ct);
                                }
                                catch (IOException closeException){
                                        try{
                                                mmSocket.close();
                                        }
                                        catch (IOException ceXC){
                                        }
                                        Toast.makeText(ct, "connessione non riuscita",  Toast.LENGTH_SHORT).show();
                                }
                        }
                }
        }

        private static void sendMessageBluetooth(String message, Context ct) {
                if (outStream == null){
                        return;
                }
                byte[] msgBuffer = message.getBytes();
                try{
                        outStream.write(msgBuffer);
                }
                catch (IOException e){
                        Toast.makeText(ct, "Messaggio non Inviato", Toast.LENGTH_SHORT).show();
                }
        }
}*/

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Context;
import android.os.Handler;
import android.os.Message;
import android.os.SystemClock;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.UUID;

class ConnectedThread extends Thread {
        private static OutputStream OutputStream;
        private static InputStream inputStream;
        private static BluetoothSocket socket;
        String macAddr = null;

        int avilableBytes=0;

        public ConnectedThread(String macAddr){
                this.macAddr = macAddr;
        }

        public void run() {
                BluetoothAdapter mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
                BluetoothDevice device=mBluetoothAdapter.getRemoteDevice(macAddr);
                UUID MY_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
                try {
                        socket=device.createInsecureRfcommSocketToServiceRecord(MY_UUID);
                        socket.connect();
                }catch(Exception e){
                        /**/
                }
                try{
                        inputStream=socket.getInputStream();
                        OutputStream = socket.getOutputStream();
                }catch (IOException e){
                        e.printStackTrace();
                }

                try{
                        int bytes;
                        while (true){
                                try{
                                        avilableBytes=inputStream.available();
                                        byte[] buffer=new byte[avilableBytes];
                                        if (avilableBytes>0){
                                                bytes=inputStream.read(buffer);
                                                final String readMessage=new String(buffer);
                                                if (bytes>=1){
                                                        System.out.println(readMessage);
                                                }
                                                else {
                                                        SystemClock.sleep(100);
                                                }
                                        }
                                }catch (IOException e){
                                        e.printStackTrace();
                                }
                        }
                }catch (Exception e){
                        e.printStackTrace();
                }
        }

        public void write(String s){
                try {
                        if (OutputStream != null)
                                OutputStream.write(s.getBytes());
                } catch (IOException e){

                }
        }

        public void disconnect() throws IOException {
                inputStream.close();
                OutputStream.close();
                socket.close();
        }
}