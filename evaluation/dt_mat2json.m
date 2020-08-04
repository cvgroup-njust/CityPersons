ndt=0;
%load('dt.mat');
for i=1:length(dt)
    bbs=dt{i};
    for ibb=1:size(bbs,1)
        ndt=ndt+1;
        bb=bbs(ibb,:);
        dt_coco(ndt).image_id=i;
        dt_coco(ndt).category_id=1;
        dt_coco(ndt).bbox=bb(1:4);
        dt_coco(ndt).score=bb(5);
    end
end

dt_string = gason(dt_coco);
fp = fopen('detections_validation.json','w');
fprintf(fp,'%s',dt_string);
fclose(fp);