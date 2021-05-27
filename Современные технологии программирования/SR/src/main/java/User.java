import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class User {
    private Integer userId;
    private String userName;

    public String getUserName() {
        return userName;
    }

    public Integer getUserAge() {
        return userAge;
    }

    public Male getUserMale() {
        return userMale;
    }

    private Integer userAge;
    private Male userMale;

    private static Map<Integer, User> users;
    private static Integer countId = 0;

    public static void setUsers(Map<Integer, User> users) {
        User.users = users;
    }

    public static Integer getCountId() {
        return countId;
    }

    public static void setCountId(Integer countId) {
        User.countId = countId;
    }

    private boolean isEmpty(){
        for (User user : users.values()){
            if (user.equals(this) && user.hashCode() == this.hashCode()){
                return true;
            }
        }
        return false;
    }

    public User(String userName, Integer userAge, Male userMale) {
        if (users == null){
            users = new HashMap<>();
        }

        this.userName = userName;
        this.userAge = userAge;
        this.userMale = userMale;
        if (!isEmpty()){
            countId++;
            this.userId = countId;
            users.put(userId, this);
        }
    }

    public static ArrayList<User> getUsers(Male male){
        ArrayList<User> result = new ArrayList<>();
        for (User entry: users.values()){
            if (entry.userMale.equals(male)){
                result.add(entry);
            }
        }
        return result;
    }

    public static ArrayList<User> getUsers(){
        ArrayList<User> result = new ArrayList<>();
        result.addAll(users.values());
        return result;
    }

    public static Integer getLength(){
        return users.size();
    }

    public static Integer getLength(Male male){
        return User.getUsers(male).size();
    }

    public static Double getMeanAge(){
        ArrayList<Integer> ages = new ArrayList<>();
        for (User entry: users.values()){
                ages.add(entry.userAge);
            }
        Double sum = 0.0;
        for(Integer age : ages){
            sum += age;
        }
        return sum / ages.size();
    }

    public static Double getMeanAge(Male male){
        ArrayList<Integer> ages = new ArrayList<>();
        ArrayList<User> usersAge = User.getUsers(male);
        for (User entry: usersAge){
            ages.add(entry.userAge);
        }
        Double sum = 0.0;
        for(Integer age : ages){
            sum += age;
        }
        return sum / ages.size();
    }

    public boolean equals(User anotherUser){
        if (this.userName.equals(anotherUser.userName) && this.userAge == anotherUser.userAge && this.userMale.equals(anotherUser.userMale)){
            return true;
        }
        return false;
    }

}
