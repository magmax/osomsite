'use strict';

angular.module('siteApp')
  .controller('PostCtrl', [
    function ($scope) {
    '$scope', 'FileRetriever',
    function ($scope, FileRetriever) {
      function init() {
        FileRetriever.fetch('/post/example1.md').then(function(post) {
          $scope.html = post;
        });
      }

      init();
    }
    }
  ]);
