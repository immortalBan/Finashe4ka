package BlogProject.java.entity;


import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@NoArgsConstructor
@Data
public class Post {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    private String title;
    private String body;

    @Column(unique = true)
    private String slug;

    @ManyToOne
    @JoinColumn(name="author_id", nullable = false)
    private User author;


}
