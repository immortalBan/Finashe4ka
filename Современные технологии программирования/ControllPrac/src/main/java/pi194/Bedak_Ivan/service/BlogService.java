package pi194.Bedak_Ivan.service;

import pi194.Bedak_Ivan.entity.Blog;
import java.util.List;

public interface BlogService {

    Blog create(Blog blog);

    Blog read(int id);

    boolean update(Blog blog, int id);

    boolean delete(int id);

    List<Blog> readAll();
}