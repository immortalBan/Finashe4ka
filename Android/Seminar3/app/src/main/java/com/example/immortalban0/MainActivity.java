package com.example.immortalban0;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.Collections;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, AdapterView.OnItemClickListener {

    TextView mainTextView;
    Button mainButton, okBtn, cncBtn, sortButton;
    EditText mainEditText;
    ListView mainListView;
    Switch removeSwitch;
    ArrayAdapter<String> mArrayAdapter;
    ArrayList<String> mNameList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        removeSwitch = findViewById(R.id.removeSwitch);
        sortButton = findViewById(R.id.sortButton);
        mainTextView = findViewById(R.id.main_textview);
        mainButton = findViewById(R.id.main_button);
        mainEditText = findViewById(R.id.main_edittext);
        mainListView = findViewById(R.id.main_listview);
        okBtn = findViewById(R.id.ok_btn);
        cncBtn = findViewById(R.id.cnc_btn);

        View.OnClickListener oclBtnListener = this::oclBtnClicked;
        View.OnClickListener sortButtonListener = this::sortButtonClicked;

        mainButton.setOnClickListener(this);
        okBtn.setOnClickListener(oclBtnListener);
        cncBtn.setOnClickListener(oclBtnListener);
        sortButton.setOnClickListener(sortButtonListener);

        mArrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, mNameList);
        mainListView.setAdapter(mArrayAdapter);
        mainListView.setOnItemClickListener(this);
    }

    @Override
    public void onClick(View v) {
        String newItemStr = mainEditText.getText().toString();
        if (newItemStr.equals("")) {
            Toast.makeText(getApplicationContext(), "Нельзя добавить пустой элемент в список", Toast.LENGTH_LONG).show();
            return;
        }
        for (String item : mNameList) {
            if (item.equals(newItemStr)) {
                String errorStr = String.format("Элемент %s уже есть в этом списке", newItemStr);
                Toast.makeText(getApplicationContext(), errorStr, Toast.LENGTH_LONG).show();
                return;
            }
        }

        mNameList.add(newItemStr);
        mArrayAdapter.notifyDataSetChanged();
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

        if (removeSwitch.isChecked()) {
            mNameList.remove(position);
            mArrayAdapter.notifyDataSetChanged();
        } else {
            Log.d("omg android", position + ": " + mNameList.get(position));
            mainTextView.setText(mNameList.get(position));
        }
    }

    private void sortButtonClicked(View v) {
        Collections.sort(mNameList);
        mArrayAdapter.notifyDataSetChanged();
    }

    private void oclBtnClicked(View v) {
        switch (v.getId()) {
            case R.id.ok_btn:
                Toast.makeText(getApplicationContext(), "Нажата кнопка ОК", Toast.LENGTH_LONG).show();
                break;
            case R.id.cnc_btn:
                Toast.makeText(getApplicationContext(), "Нажата кнопка Cancel", Toast.LENGTH_LONG).show();
                break;
        }

    }
}