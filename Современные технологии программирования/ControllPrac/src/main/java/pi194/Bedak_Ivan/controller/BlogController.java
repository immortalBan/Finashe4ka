package pi194.Bedak_Ivan.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import java.util.List;

import pi194.Bedak_Ivan.entity.Blog;
import pi194.Bedak_Ivan.service.BlogService;


@RestController
public class BlogController {
    private final BlogService blogService;

    @Autowired
    public BlogController(BlogService blogService) {
        this.blogService = blogService;
    }

    @GetMapping(value = "/blog")
    public ResponseEntity<List<Blog>> read() {
        final List<Blog> blogs = blogService.readAll();
        return blogs != null && !blogs.isEmpty()
                ? new ResponseEntity<>(blogs, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @GetMapping(value = "/blog/{id}")
    public ResponseEntity<Blog> read(@PathVariable(name = "id") int id) {
        final Blog blog = blogService.read(id);
        return blog != null
                ? new ResponseEntity<>(blog, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @PostMapping(value = "/blog")
    public ResponseEntity<?> create(@RequestBody Blog blog) {
        Blog newBlog = blogService.create(blog);
        return new ResponseEntity<>(newBlog, HttpStatus.CREATED);
    }


    @PutMapping(value = "/blog/{id}")
    public ResponseEntity<Blog> put(@PathVariable(name = "id") int id, @RequestBody Blog mewBlog) {

        boolean response = blogService.update(mewBlog, id);
        if (response) {
            Blog newBlogId = blogService.read(id);
            return new ResponseEntity<>(newBlogId, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }


    @DeleteMapping(value = "/blog/{id}")
    public ResponseEntity<?> delete(@PathVariable(name = "id") int id) {
        final Blog blog = blogService.read(id);
        if (blog != null) {
            blogService.delete(id);
            return new ResponseEntity<>(HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}