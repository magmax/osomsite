'use strict';

angular.module('siteApp')
  .controller('NavbarCtrl', function ($scope, $location) {
    $scope.isActive = function (viewLocation) {
      return (viewLocation === $location.path());
    };
  });
