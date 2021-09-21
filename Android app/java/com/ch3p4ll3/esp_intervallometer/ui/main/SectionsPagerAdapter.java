package com.ch3p4ll3.esp_intervallometer.ui.main;

import android.content.Context;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import com.ch3p4ll3.esp_intervallometer.Bulb;
import com.ch3p4ll3.esp_intervallometer.BulbIntervallometer;
import com.ch3p4ll3.esp_intervallometer.R;
import com.ch3p4ll3.esp_intervallometer.Intervallometer;
import com.ch3p4ll3.esp_intervallometer.singleShot;
import com.ch3p4ll3.esp_intervallometer.timerBulb;

/**
 * A [FragmentPagerAdapter] that returns a fragment corresponding to
 * one of the sections/tabs/pages.
 */
public class SectionsPagerAdapter extends FragmentPagerAdapter {

    @StringRes
    private static final int[] TAB_TITLES = new int[]{R.string.tab_text_1, R.string.tab_text_2, R.string.tab_text_3, R.string.tab_text_4, R.string.tab_text_5};
    private final Context mContext;
    private String macAddr;

    public SectionsPagerAdapter(Context context, FragmentManager fm, String macAddr) {
        super(fm);
        mContext = context;
        this.macAddr = macAddr;
    }

    @Override
    public Fragment getItem(int position) {
        Fragment fragment = null;

        switch (position){
            case 0:
                fragment = singleShot.newInstance(macAddr);
                break;

            case 1:
                fragment = Bulb.newInstance(macAddr);
                break;

            case 2:
                fragment = timerBulb.newInstance(macAddr);
                break;

            case 3:
                fragment = Intervallometer.newInstance(macAddr);
                break;

            case 4:
                fragment = BulbIntervallometer.newInstance(macAddr);
                break;

            default:
                fragment = new PlaceholderFragment();
        }

        return fragment;
    }

    @Nullable
    @Override
    public CharSequence getPageTitle(int position) {
        return mContext.getResources().getString(TAB_TITLES[position]);
    }

    @Override
    public int getCount() {
        // Show 2 total pages.
        return TAB_TITLES.length;
    }
}