package com.example.immortalban0;

import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {

    TextView tvColor, tvSize, tvFont;

    final int MENU_COLOR_RED = 1;
    final int MENU_COLOR_GREEN = 2;
    final int MENU_COLOR_BLUE = 3;

    final int MENU_SIZE_22 = 4;
    final int MENU_SIZE_26 = 5;
    final int MENU_SIZE_30 = 6;

    final int MENU_FONT_MONOSPACE = 7;
    final int MENU_FONT_SANS_SERIF = 8;
    final int MENU_FONT_ITALIC = 9;


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvColor = (TextView) findViewById(R.id.tvColor);
        tvSize = (TextView) findViewById(R.id.tvSize);
        tvFont = (TextView) findViewById(R.id.tvFont);

        // для tvColor и tvSize необходимо создавать контекстное меню
        registerForContextMenu(tvColor);
        registerForContextMenu(tvSize);
        registerForContextMenu(tvFont);

    }


    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        switch (v.getId()) {

            case R.id.tvColor:
                menu.add(0, MENU_COLOR_RED, 0, "Red");
                menu.add(0, MENU_COLOR_GREEN, 0, "Green");
                menu.add(0, MENU_COLOR_BLUE, 0, "Blue");
                break;

            case R.id.tvSize:
                menu.add(0, MENU_SIZE_22, 0, "22");
                menu.add(0, MENU_SIZE_26, 0, "26");
                menu.add(0, MENU_SIZE_30, 0, "30");
                break;

            case R.id.tvFont:
                menu.add(0, MENU_FONT_MONOSPACE, 0, "Monospace");
                menu.add(0, MENU_FONT_SANS_SERIF, 0, "Sans-serif");
                menu.add(0, MENU_FONT_ITALIC, 0, "Italic");
                break;
        }
    }

    @Override
    public boolean onContextItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            // пункты меню для tvColor
            case MENU_COLOR_RED:
                tvColor.setTextColor(Color.RED);
                tvColor.setText("Text color");
                break;
            case MENU_COLOR_GREEN:
                tvColor.setTextColor(Color.GREEN);
                tvColor.setText("Text color");
                break;
            case MENU_COLOR_BLUE:
                tvColor.setTextColor(Color.BLUE);
                tvColor.setText("Text color");
                break;
            case MENU_SIZE_22:
                tvSize.setTextSize(22);
                tvSize.setText("Text size");
                break;
            case MENU_SIZE_26:
                tvSize.setTextSize(26);
                tvSize.setText("Text size");
                break;
            case MENU_SIZE_30:
                tvSize.setTextSize(30);
                tvSize.setText("Text size");
                break;
            case MENU_FONT_MONOSPACE:
                tvFont.setTypeface(Typeface.MONOSPACE, Typeface.NORMAL);
                break;
            case MENU_FONT_SANS_SERIF:
                tvFont.setTypeface(Typeface.SANS_SERIF, Typeface.NORMAL);
                break;
            case MENU_FONT_ITALIC:
                tvFont.setTypeface(Typeface.DEFAULT, Typeface.ITALIC);
                break;
        }
        return super.onContextItemSelected(item);
    }

}