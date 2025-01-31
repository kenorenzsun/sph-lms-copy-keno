/* eslint-disable multiline-ternary */
import { useAppDispatch, useAppSelector } from '@/app/hooks';
import { changeEditMode, reset as courseReset } from '@/features/course/courseSlice';
import { setIsTabValid } from '@/features/tab/tabSlice';
import { useGetCourseQuery } from '@/services/courseAPI';
import EditModeButtons from '@/src/shared/components/Button/EditModeButtons';
import { courseSchema } from '@/src/shared/utils/validationSchemas';
import { yupResolver } from '@hookform/resolvers/yup';
import { useRouter } from 'next/router';
import { type FC, Fragment, useEffect } from 'react';
import { useForm } from 'react-hook-form';

const EditSettingsButton: FC = () => {
  const { query } = useRouter();
  const { activeTab } = useAppSelector((state) => state.tab);
  const { editMode, values } = useAppSelector((state) => state.course);
  const { data: course } = useGetCourseQuery(query.id, {
    skip: query.id === undefined,
  });

  const dispatch = useAppDispatch();
  const defaultValues = {
    ...values,
    category: values.category.map(({ name, id }) => ({
      label: name,
      value: id,
    })),
  };

  const { trigger, reset } = useForm({
    resolver: yupResolver(courseSchema),
    mode: 'onChange',
    defaultValues,
  });

  const handleCancel = (): void => {
    dispatch(courseReset(course));
    dispatch(setIsTabValid(true));
    dispatch(changeEditMode(false));
  };

  const onSave = async (): Promise<void> => {
    let areInputsValid = true;
    if (values.image) {
      areInputsValid = await trigger(['image', 'name', 'category']);
    } else {
      areInputsValid = await trigger(['name', 'category']);
    }

    const isValidated = areInputsValid && values.lessons.length > 0;
    dispatch(setIsTabValid(isValidated));

    if (isValidated) {
      dispatch(changeEditMode(false));
      // Please place the logic for saving the course edit form here
      alert('The information provided has been saved');
    }
  };

  useEffect(() => {
    reset(defaultValues);
  }, [values]);

  return (
    <Fragment>
      {activeTab === 2 && (
        <EditModeButtons
          editMode={editMode}
          onCancel={handleCancel}
          onSave={onSave}
          onEdit={() => dispatch(changeEditMode(true))}
        />
      )}
    </Fragment>
  );
};

export default EditSettingsButton;
