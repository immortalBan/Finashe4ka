package com.immortalBan0;

public class StringBuilderClass {

    private StringBuilder mainString;
    private StringBuilder prevString;

    public StringBuilderClass(String string) {
        this.setMainString(new StringBuilder(string));

    }

    public StringBuilder getMainString() {
        return mainString;
    }

    public void setMainString(StringBuilder mainString) {
        this.mainString = new StringBuilder(mainString);
    }

    public StringBuilder getPrevString() {
        return prevString;
    }

    public void setPrevString(StringBuilder prevString) {
        this.prevString = new StringBuilder(prevString);
    }

    public String substring(int leftIndex) {
        this.setPrevString(this.mainString);
        return this.mainString.substring(leftIndex);
    }

    public String substring(int leftIndex, int rightIndex) {
        this.setPrevString(this.mainString);
        return this.mainString.substring(leftIndex, rightIndex);
    }

    public void undo() {
        this.setMainString(this.prevString);
    }

    public StringBuilder replace (int leftIndex, int rightIndex, String replaceString) {
        this.setPrevString(this.mainString);
        this.setMainString(this.mainString.replace(leftIndex, rightIndex, replaceString));
        return this.mainString;
    }

    @Override
    public String toString() {
        return this.mainString.toString();
    }
}
