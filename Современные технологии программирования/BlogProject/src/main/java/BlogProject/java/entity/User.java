package BlogProject.java.entity;

import lombok.NoArgsConstructor;
import lombok.Data;

import javax.persistence.*;
import java.util.Set;

@Entity
@NoArgsConstructor
@Data
@Table(name = "t_user")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(unique = true)
    private String login;

    @Column(unique = true)
    private String email;

    private String password;

    private boolean isActivated;

    @OneToMany(mappedBy = "author")
    private Set<Post> posts;

}
