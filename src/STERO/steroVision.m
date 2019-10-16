% 
% clc;
% clear all;
% feature('locale')
% function [cor1,cor2] = steroVision(centroids,centroids_t)
function [cor1,fdx] = steroVision(centroids)
% I1 = imread('l1.png');%¶ÁÈ¡×óÓÒÍ¼Æ¬
% I2 = imread('r1.png');
% I1 = imread('left_cam.png');%¶ÁÈ¡×óÓÒÍ¼Æ¬
% I2 = imread('right_cam.png');
I1 = imread('3l.png');%¶ÁÈ¡×óÓÒÍ¼Æ¬
I2 = imread('3r.png');

% size(centroids)
% size(centroids_t)
% centroids(1)
% centroids_t

% figure
% imshowpair(I1, I2, 'montage');
% title('Original Images');

%¼ÓÔØstereoParameters¶ÔÏó¡£
load('calibrationSession.mat'); %¼ÓÔØÄã±£´æµÄÏà»ú±ê¶¨µÄmat
[J1, J2] = rectifyStereoImages(I1, I2, calibrationSession.CameraParameters);
% 
% figure
% imshowpair(J1, J2, 'montage');
% title('Undistorted Images');

%222222
% figure; imshow(cat(3, J1(:,:,1), J2(:,:,2:3)), 'InitialMagnification', 50);%Í¼ÏñÏÔÊ¾50%

%3333
% WL1 = abs(imfilter(rgb2gray(J1), fspecial('Laplacian'), 'replicate', 'conv'));
% WL2 = abs(imfilter(rgb2gray(J2), fspecial('Laplacian'), 'replicate', 'conv'));
% 
% WL1(WL1(:)>=WL2(:)) = 1;WL1(WL1(:)<WL2(:)) = 0;
% WL2(WL1(:)>=WL2(:)) = 0;WL2(WL1(:)<WL2(:)) = 1;
% 
% J_F(:,:,1) = J1(:,:,1).*WL1+J2(:,:,1).*WL2;
% J_F(:,:,2) = J1(:,:,2).*WL1+J2(:,:,2).*WL2;
% J_F(:,:,3) = J1(:,:,3).*WL1+J2(:,:,3).*WL2;
% figure; imshow(J_F, 'InitialMagnification', 50);%Í¼ÏñÏÔÊ¾50%

%44444
disparityMap = disparity(rgb2gray(J1), rgb2gray(J2), 'BlockSize',15,'DisparityRange',[0,320],'BlockSize',15,'ContrastThreshold',0.5,'UniquenessThreshold',15);
% disparityMap = disparitySGM(rgb2gray(J1), rgb2gray(J2),'DisparityRange',[0,400],'UniquenessThreshold',20);
% disparityMap
%5555
% centroids = [825,612]
% centroids_t = [770,612]

% figure;imshow(disparityMap, [0, 400]);
% title('Disparity Map');
% colormap jet
% colorbar
% hold on
% plot(centroids(1,1),centroids(1,2),'y-o','MarkerSize',10,'MarkerFaceColor','r');

%6666
pointCloud3D = reconstructScene(disparityMap, calibrationSession.CameraParameters);
pointCloud3D = double(pointCloud3D);
pointCloud3D = pointCloud3D/1000;

%7777

Z = double(pointCloud3D(:,:,3));
mask = repmat(Z> 0&Z <1000,[1,1,3]);
J1(~mask)= 0;

figure;imshow(J1,'InitialMagnification',100)
hold on
plot(centroids(1),centroids(2),'y-o','MarkerSize',10,'MarkerFaceColor','r')
% plot(centroids_t(1),centroids_t(2),'y-o','MarkerSize',10,'MarkerFaceColor','r');
% plot(centroids(1,1),centroids(1,2),'y-o','MarkerSize',10,'MarkerFaceColor','r');
% plot(centroids_t(1,1),centroids_t(1,2),'y-o','MarkerSize',10,'MarkerFaceColor','r');
% plot(centroids{1,1},centroids{1,2},'y-o','MarkerSize',10,'MarkerFaceColor','r');
% plot(centroids_t{1,1},centroids_t{1,2},'y-o','MarkerSize',10,'MarkerFaceColor','r');


centroidsIdx = sub2ind(size(disparityMap), centroids(2), centroids(1));
% centroidsIdx = sub2ind(size(disparityMap), centroids{:, 2}, centroids{:, 1});
X = pointCloud3D(:, :, 1);
Y = pointCloud3D(:, :, 2);
Z = pointCloud3D(:, :, 3);
centroids3D = [X(centroidsIdx), Y(centroidsIdx), Z(centroidsIdx)];

% centroidsIdx_t = sub2ind(size(disparityMap), centroids_t(2), centroids_t(1));
% % centroidsIdx_t = sub2ind(size(disparityMap), centroids_t{:, 2}, centroids_t{:, 1});
% X = pointCloud3D(:, :, 1);
% Y = pointCloud3D(:, :, 2);
% Z = pointCloud3D(:, :, 3);
% centroids3D_t = [X(centroidsIdx_t), Y(centroidsIdx_t), Z(centroidsIdx_t)];

cor1 = centroids3D;
% cor2 = centroids3D_t

% diff = abs(centroids3D(1,1)-centroids3D_t(1,1))
% dists = sqrt(sum(centroids3D .^ 2))
fdx = (calibrationSession.CameraParameters.CameraParameters1.IntrinsicMatrix(1)+calibrationSession.CameraParameters.CameraParameters1.IntrinsicMatrix(5))*0.5;
end











