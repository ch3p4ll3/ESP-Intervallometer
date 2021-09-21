package com.ch3p4ll3.esp_intervallometer;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link singleShot#newInstance} factory method to
 * create an instance of this fragment.
 */
public class singleShot extends Fragment  {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "macAddr";

    // TODO: Rename and change types of parameters
    private String macAdd;
    private Button singleShot_btn;

    public singleShot() {
        // Required empty public constructor
    }

    public static singleShot newInstance(String macAddress) {
        singleShot fragment = new singleShot();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, macAddress);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            macAdd = getArguments().getString(ARG_PARAM1);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_single_shot, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        singleShot_btn = (Button) getView().findViewById(R.id.singleShot_btn);
        singleShot_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getContext(), "Single shot", Toast.LENGTH_SHORT).show();
                //BlManagement.connect(view.getContext(), macAdd, "singleShot#");
                MainActivity.sendSingleShot();
            }
        });
    }
}