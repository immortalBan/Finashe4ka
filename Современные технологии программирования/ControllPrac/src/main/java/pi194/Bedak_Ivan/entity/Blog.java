package pi194.Bedak_Ivan.entity;

import lombok.*;
import javax.persistence.*;

@Entity
@Data
@NoArgsConstructor
public class Blog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String text;
    private String creationDate;
    private String updateDate;
    private String author;
    private String teg;



}