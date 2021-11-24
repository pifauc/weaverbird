import { FilterSimpleCondition } from '@/lib/steps';

import { Mongo40Translator } from './mongo4';

export class Mongo42Translator extends Mongo40Translator {
  static label = 'Mongo 4.2';

  protected unsupportedOperatorsInConditions: FilterSimpleCondition['operator'][] = [
    // TODO: for now we raised an execption until this two operator will be developped
    'from',
    'until',
  ];
}
