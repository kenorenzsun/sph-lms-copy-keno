import Breadcrumbs from '@/src/shared/components/Breadcrumbs';
import Tabs from '@/src/shared/components/Tabs';
import Tab from '@/src/shared/components/Tabs/Tab';
import Container from '@/src/shared/layouts/Container';
import { Fragment } from 'react';
import LearningPathLearnersSection from '@/src/sections/learning-paths/LearnersSection';
import LearningPathContentSection from '@/src/sections/learning-paths/ContentSection';
import SettingsSection from '@/src/sections/learning-paths/settingsSection';
import EditSettingsButton from '@/src/sections/learning-paths/settingsSection/EditSettingsButton';

interface LearningPath {
  id: number;
  name: string;
}

const LearningPathContent: React.FC = () => {
  const learningPath: LearningPath = {
    id: 1,
    name: 'Learning Path 1',
  };

  const paths = [
    {
      text: 'Learning Paths',
      url: '/trainer/learning-paths',
    },
    {
      text: learningPath?.name,
      url: `/trainer/learning-paths/${learningPath.id}`,
    },
  ];

  return (
    <Fragment>
      <div className="ml-5 mt-5">
        <Breadcrumbs paths={paths} />
        <Container className="px-28">
          <div className="text-[20px] font-semibold my-5 text-textGray flex justify-between line-clamp-1">
            <h1>{learningPath?.name}</h1>
            <EditSettingsButton />
          </div>
          <Tabs>
            <Tab title="Content">
              <LearningPathContentSection />
            </Tab>
            <Tab title="Learners">
              <LearningPathLearnersSection />
            </Tab>
            <Tab title="Settings">
              <SettingsSection />
            </Tab>
          </Tabs>
        </Container>
      </div>
    </Fragment>
  );
};

export default LearningPathContent;
