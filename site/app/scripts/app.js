'use strict';

angular.module('siteApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/posts', {
        templateUrl: 'views/post_list.html',
        controller: 'PostListCtrl'
      })
      .when('/post/:filename', {
        templateUrl: 'views/post.html',
        controller: 'PostCtrl'
      })
      .when('/contact', {
        templateUrl: 'views/contact.html',
        controller: 'MainCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
