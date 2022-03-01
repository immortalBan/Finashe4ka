package com.example.immortalban0;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    TextView mainTextView;
    Button mainButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainTextView = findViewById(R.id.main_textview);
        mainTextView.setText("Семинар 2, выполнил Бедак Иван.");
        mainButton = findViewById(R.id.main_button);
        mainButton.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        mainTextView.setText("Вы нажали на кнопку");
    }
}