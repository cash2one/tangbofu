module.exports = function(grunt) {
    /*
    合并文件：grunt-contrib-concat
    语法检查：grunt-contrib-jshint
    Scss 编译：grunt-contrib-sass
    压缩文件：grunt-contrib-uglify
    监听文件变动：grunt-contrib-watch
    建立本地服务器：grunt-contrib-connect
    */
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        meta: {
            basePath: './',
            cssSrcPath: 'scss/',
            cssDeployPath: 'css/',
            JsDir: 'js/',
            DepDir: 'build/',
        },
        jshint: {
            files: ['Gruntfile.js', 'src/**/*.js', 'test/**/*.js'],
            options: {
                globals: {
                    jQuery: true
                }
            }
        },
        concat: {
            options: {
                stripBanners: true
            },
            dist: {
                src: [
                    '<%= meta.JsDir %>/jquery.min.js', 
                    '<%= meta.JsDir %>/jquery.lazyload.min.js',
                    'tether/js/tether.min.js',
                    'bootstrap-v4/js/bootstrap.min.js'
                ],
                dest: '<%= meta.DepDir %>/<%= pkg.name %>.js'
            },
            distcss: {
                src: [
                    'bootstrap-v4/css/bootstrap.min.css', 
                    'font-awesome/css/font-awesome.min.css',
                    'css/main.css'
                ],
                dest: 'css/<%= pkg.name %>.css'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n', 
            },
            // 子任务名称
            build: {
                src: 'build/<%= pkg.name %>.js',
                dest: 'build/<%= pkg.name %>.min.js'
            },
        },
        sass: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'styles',
                    src: ['scss/*.scss'],
                    dest: 'css/',
                    ext: '.css'
                }]
            }
        },
        watch: {
            css: {
                files: 'scss/*.scss',
                tasks: ['sass:dist'],
                options: {
                    //livereload: true,
                },
            },

            files: ['<%= jshint.files %>'],
            tasks: ['jshint'],
        }

    });


    // 加载包含 "uglify" 任务的插件。
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // 默认被执行的任务列表。默认的任务名字为default
    //grunt.registerTask('default', ['uglify']);

    // 非默认的任务,我们需要输入 grunt compress 命令来执行这条 task，
    //grunt.registerTask('compress', ['uglify:build']); 
    grunt.registerTask('css', ['watch:css']);
    //grunt.registerTask('default', ['concat:dist', 'uglify:build']);
    grunt.registerTask('default', ['concat:dist', 'concat:distcss']);
};
