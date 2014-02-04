'use strict';

angular.module('siteApp')
  .controller('PostListCtrl', function ($scope) {
    $scope.posts = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
