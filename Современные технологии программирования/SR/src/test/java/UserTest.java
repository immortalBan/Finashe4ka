import junit.framework.TestCase;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class UserTest extends TestCase {

    private User user;
    private User user1;
    private User user2;

    @Before
    public void setUp() throws Exception {
        user = new User("Иван", 19, Male.MALE);
        user1 = new User("Баир", 19, Male.MALE);
        user2 = new User("Вера", 18, Male.FEMALE);
    }

    @After
    public void tearDown() throws Exception {
        User.setUsers(new HashMap<>());
        User.setCountId(0);
    }

    @Test
    public void testGetUsers() {
        ArrayList<User> expected = User.getUsers();

        ArrayList<User> actual = new ArrayList<>();
        actual.add(user);
        actual.add(user1);
        actual.add(user2);

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testTestGetUsers(Male male) {
        ArrayList<User> expected = User.getUsers(male);

        ArrayList<User> actual = new ArrayList<>();
        if (male == Male.MALE){
            actual.add(user);
            actual.add(user1);
        } else {
            actual.add(user2);
        }

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testGetLength() {
        Integer expected = User.getLength();

        ArrayList<User> actualArray = new ArrayList<>();
        actualArray.add(user);
        actualArray.add(user1);
        actualArray.add(user2);

        Integer actual = actualArray.size();

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testTestGetLength() {
        Male male = Male.MALE;
        Integer expected = User.getLength(male);

        ArrayList<User> actualArray = new ArrayList<>();
        if (male == Male.MALE){
            actualArray.add(user);
            actualArray.add(user1);
        } else {
            actualArray.add(user2);
        }

        Integer actual = actualArray.size();

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testGetMeanAge() {
        Double expected = User.getMeanAge();
        System.out.println(User.getUsers());

        ArrayList<User> actualArray = new ArrayList<>();
        actualArray.add(user);
        actualArray.add(user1);
        actualArray.add(user2);

        Double actualSum = 0.0;
        for (User u: actualArray){
            actualSum += u.getUserAge();
        }

        Double actual = actualSum / actualArray.size();

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testTestGetMeanAge() {
        Male male = Male.FEMALE;
        Double expected = User.getMeanAge(male);

        ArrayList<User> actualArray = new ArrayList<>();
        if (male == Male.MALE){
            actualArray.add(user);
            actualArray.add(user1);
        } else {
            actualArray.add(user2);
        }

        Double actualSum = 0.0;
        for (User u: actualArray){
            actualSum += u.getUserAge();
        }

        Double actual = actualSum / actualArray.size();

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testTestEquals() {
        User user4 = new User("Иван", 19, Male.MALE);
        boolean expected = user.equals(user1);
        boolean actual = false;
        Assert.assertEquals(expected, actual);

        expected = user.equals(user4);
        actual = true;
        Assert.assertEquals(expected, actual);


    }
}