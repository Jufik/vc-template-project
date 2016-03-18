var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var notify = require("gulp-notify");
var livereload = require('gulp-livereload');

gulp.task('sass', function() {

  return gulp
    .src('assets/{{ project_name }}/scss/*.scss')
    .pipe(sourcemaps.init())
    .pipe(sass({ 
        // outputStyle: 'compressed'
    }).on('error', sass.logError))
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest('assets/{{ project_name }}/css'))
    .pipe(notify("style.css generated"))
    .pipe(livereload());
});

gulp.task('default',function() {
    return gulp.watch('assets/{{ project_name }}/scss/**/*.scss',['sass']);
});

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('assets/{{ project_name }}/scss/**/*.scss', ['sass']);
});