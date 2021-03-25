package pi194.Bedak_Ivan.repository;

import pi194.Bedak_Ivan.entity.Blog;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BlogRepository extends JpaRepository<Blog, Long> {
    List<Blog> findByLastName(String lastName);
    Blog findById(long id);
}
