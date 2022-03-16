package com.example.immortalban0;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    TextView mainTextView;
    Button guessBtn, resetBtn;
    EditText mainEditText;
    int number;
    boolean win;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        win = false;
        number = (int) (Math.random() * 99 + 1);
        System.out.println(number);

        mainTextView = findViewById(R.id.main_textview);
        mainEditText = findViewById(R.id.main_edittext);
        guessBtn = findViewById(R.id.guess_btn);
        resetBtn = findViewById(R.id.reset_btn);
        resetBtn.setVisibility(View.INVISIBLE);

        guessBtn.setOnClickListener(this);
        resetBtn.setOnClickListener(this::resetListener);

    }

    @Override
    public void onClick(View v) {
        int num;
        String newItemStr = mainEditText.getText().toString();
        if (newItemStr.equals("")) {
            Toast.makeText(getApplicationContext(), "Нельзя добавить пустой элемент в список", Toast.LENGTH_LONG).show();
            return;
        }
        if (win == true){
            Toast.makeText(getApplicationContext(), "Вы уже отгадали число, перезапустите игру", Toast.LENGTH_LONG).show();
            return;
        }
        try {
            num = Integer.parseInt(newItemStr);
        } catch (NumberFormatException e) {
            return;
        }
        if ((num > 100) || (num < 1)) {
            Toast.makeText(getApplicationContext(), "Вы ввели значение вне интервала", Toast.LENGTH_LONG).show();
            return;
        }

        makeGuess(num);

    }

    public void makeGuess(int num){
        if (num == number){
            win = true;
            resetBtn.setVisibility(View.VISIBLE);
            Toast.makeText(getApplicationContext(), "Вы угадали значение!\nПоздравляю!", Toast.LENGTH_LONG).show();
            return;
        }
        if (num < number){
            Toast.makeText(getApplicationContext(), "Вы назвали число меньше загаданного\nПопробуйте еще раз", Toast.LENGTH_LONG).show();
            return;
        }
        if (num > number){
            Toast.makeText(getApplicationContext(), "Вы назвали число больше загаданного\nПопробуйте еще раз", Toast.LENGTH_LONG).show();
            return;
        }
    }

    public void resetListener(View v){
        win = false;
        number = (int) (Math.random() * 99 + 1);
        mainEditText.setText("");
        resetBtn.setVisibility(View.INVISIBLE);
        Toast.makeText(getApplicationContext(), "Игра перезапущена", Toast.LENGTH_LONG).show();
        return;
    }

}