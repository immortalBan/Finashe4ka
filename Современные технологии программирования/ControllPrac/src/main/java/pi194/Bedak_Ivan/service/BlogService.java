package pi194.Bedak_Ivan.service;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pi194.Bedak_Ivan.entity.Blog;
import java.util.List;

@Repository
public interface BlogService extends JpaRepository<Blog, Long> {

    Blog create(Blog blog);

    Blog read(int id);

    boolean update(Blog blog, int id);

    boolean delete(int id);

    List<Blog> readAll();
}