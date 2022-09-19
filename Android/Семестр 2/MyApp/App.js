import { Image, StyleSheet, Text, View, Button } from "react-native";

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.textContainer}>Hello world!</Text>
      <Text style={styles.textContainer}>Выполнил Бедак Иван ПИ19-2</Text>
      <Button title="Нажми меня" />
      <Image source={require("./ok.png")} style={styles.image} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  textContainer: {
    marginTop: 5,
    marginBottom: 5,
    color: "#000",
  },
  image: {
    justifyContent: "center",
    width: 50,
    height: 50,
    resizeMode: "contain",
    marginTop: 20,
  },
});
