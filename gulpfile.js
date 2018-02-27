'use strict';

var gulp = require('gulp');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var jshint = require('gulp-jshint');
var browserSync = require('browser-sync');

var STATIC_DIR = './app/static/';
var JS_DIR = STATIC_DIR + 'js/';
var CSS_DIR = STATIC_DIR + 'css/';
var SCSS_DIR = STATIC_DIR + 'scss/';

// define the default task and add the watch task to it
gulp.task('default', function() {
  // Start up BrowserSync and have it proxy through our Flask App
  browserSync.init({
    proxy: "localhost:8080"
  });

  gulp.watch(JS_DIR + 'app.js', ['jshint']);
  gulp.watch(JS_DIR + 'app.js', ['minify']);
  // Here we watch for changes to our SCSS file and on change reload browser
  // via BrowserSync
  gulp.watch(SCSS_DIR + 'styles.scss', ['sass']).on('change', browserSync.reload);;
});

// configure minification task
gulp.task('minify', function() {
  return gulp.src(JS_DIR + 'app.js')
    // This will output the non-minified version
    // .pipe(gulp.dest(DEST))
    .pipe(uglify())
    .pipe(rename({ extname: '.min.js' }))
    .pipe(gulp.dest(JS_DIR));
});

// configure SASS compile task
gulp.task('sass', function() {
  return gulp.src(SCSS_DIR + 'styles.scss')
    // .pipe(sass(SCSS_DIR + '**/*.scss'))
    // other outputStyle options 'nested', 'expanded', 'compressed', 'compact'
    .pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError))
    .pipe(gulp.dest('./app/static/css/'));
});

// configure the jshint task
// gulp.task('jshint', function() {
//   // return gulp.src(STATIC_DIR + 'js/**/*.js')
//   return gulp.src(JS_DIR + 'app.js')
//     .pipe(jshint())
//     .pipe(jshint.reporter('jshint-stylish'));
//     // .pipe(jshint.reporter('default'));
// });