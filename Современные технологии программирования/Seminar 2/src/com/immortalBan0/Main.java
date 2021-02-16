package com.immortalBan0;

public class Main {

    public static void main(String[] args) {
        String numbers = "0123456789";

        StringBuilderClass sb = new StringBuilderClass(numbers);

        System.out.println(sb.substring(3)); //3456789
        System.out.println(sb.substring(4, 8)); //4567
        System.out.println(sb.replace(3, 5, "ABCDE"));

        sb.undo();

        System.out.println(sb);
    }
}
